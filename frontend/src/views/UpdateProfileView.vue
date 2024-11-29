<script setup>
import { computed, reactive } from "vue";
import { useToast } from "vue-toastification";
import ImageUploader from "@/components/ImageUploader.vue";
import UploadTrigger from "@/components/UploadTrigger.vue";
import axios from "axios";
const user = JSON.parse(localStorage.getItem("user"));
const form = reactive({
  email: user.email,
  username: user.username,
  bio: user.bio,
  profile_picture: user.profile_picture,
});
// const state = reactive({
//   user: {},
//   isLoading: true,
// });

const toast = useToast();

const handleSubmit = async () => {
  const updatedProfile = {
    email: form.email,
    username: form.username,
    bio: form.bio,
    profile_picture: form.profile_picture,
  };

  try {
    const response = await axios.put(
      `/api/user/profile/update/`,
      updatedProfile,
      {
        headers: {
          Authorization: `Bearer ${
            JSON.parse(localStorage.getItem("token")).access
          }`,
        },
      }
    );
    toast.success("Profile Updated Successfully");
    window.location.href = "/profile";
  } catch (error) {
    let errors = Object.entries(error.response.data.errors);
    errors = errors.flat(Infinity);
    console.log(errors, "errors");
    const errorString = `${errors[1]}`;
    console.log("Error fetching user", error.response.data.errors);
    toast.error(errorString, "User Was Not Updated");
  }
};

// onMounted(async () => {
//   try {
//     const response = await axios.get(`/api/user/profile`);
//     state.user = response.data;
//     // Populate inputs
//   } catch (error) {
//     console.error("Error fetching user", error);
//   } finally {
//     state.isLoading = false;
//   }
// });
</script>

<template>
  <section class="my-auto dark:bg-gray-900">
    <div class="lg:w-[80%] md:w-[90%] xs:w-[96%] mx-auto flex gap-4">
      <div
        class="lg:w-[88%] md:w-[80%] sm:w-[88%] xs:w-full mx-auto shadow-2xl p-4 rounded-xl h-fit self-center dark:bg-gray-800/40">
        <div class="">
          <form @submit.prevent="handleSubmit">
            <div
              class="relative min-h-[200px] w-full rounded-sm bg-[url('https://images.unsplash.com/photo-1449844908441-8829872d2607?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NzEyNjZ8MHwxfHNlYXJjaHw2fHxob21lfGVufDB8MHx8fDE3MTA0MDE1NDZ8MA&ixlib=rb-4.0.3&q=80&w=1080')] bg-cover bg-center bg-no-repeat items-center py-[2rem]">
              <ImageUploader
                :trigger="UploadTrigger"
                :image_url="user.profile_picture" />
            </div>
            <div
              class="flex lg:flex-row md:flex-col sm:flex-col xs:flex-col gap-x-[2rem] justify-center w-full">
              <div class="w-full mb-4 mt-6">
                <label for="email" class="mb-2 dark:text-gray-300">
                  Email</label
                >
                <input
                  type="email"
                  v-model="form.email"
                  name="email"
                  id="email"
                  class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800"
                  placeholder="name@company.com" />
              </div>
              <div class="w-full mb-4 lg:mt-6">
                <label for="username" class="dark:text-gray-300">
                  Username</label
                >
                <input
                  type="text"
                  v-model="form.username"
                  name="username"
                  id="username"
                  class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800"
                  placeholder="Username" />
              </div>
            </div>

            <div class="w-full mb-4 lg:mt-2">
              <label
                for="bio"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your bio</label
              >
              <textarea
                v-model="form.bio"
                id="bio"
                name="bio"
                rows="6"
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Your bio here..."></textarea>
            </div>

            <div
              class="w-full rounded-lg bg-primary mt-4 text-white text-lg font-semibold hover:bg-primary-dark">
              <button type="submit" class="w-full p-4">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
