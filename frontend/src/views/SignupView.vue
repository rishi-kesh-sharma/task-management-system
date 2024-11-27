<script setup>
import { RouterLink, useRouter } from "vue-router";
import Logo from "@/assets/img/logo.png";
import { reactive } from "vue";
import { useToast } from "vue-toastification";
import axios from "axios";

const toast = useToast();

const form = reactive({
  email: "",
  username: "",
  bio: "",
  profile_picture: "",
  password: "",
  password2: "",
});

const handleSubmit = async () => {
  try {
    const body = {
      email: form.email,
      username: form.username,
      bio: form.bio,
      profile_picture: form.profile_picture,
      password: form.password,
      password2: form.password2,
    };
    const response = await axios.post(`/api/user/register/`, body);
    const data = response.data;
    const profileResponse = await axios.get(`/api/user/profile`, {
      headers: {
        Authorization: `Bearer ${data.token.access}`,
      },
    });
    console.log(data, "data");

    // clear localstorage
    localStorage.clear();
    const token = JSON.stringify(data.token);
    const profileData = JSON.stringify(profileResponse.data);

    // set the items to localstorage
    localStorage.setItem("token", token);
    localStorage.setItem("user", profileData);
    localStorage.setItem("isAuthenticated", true);
    window.location.href = "/";
  } catch (err) {
    toast.error(
      err.response.data.errors.non_field_errors[0] || "Error occurred"
    );
    console.log(err.response.data.errors.non_field_errors[0], "errors");
  }
};
</script>

<template>
  <section class="bg-gray-50 dark:bg-gray-900">
    <div
      class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <RouterLink
        to="/"
        class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
        <img class="w-8 h-8 mr-2" :src="Logo" alt="logo" />
        Taskify
      </RouterLink>
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-[700px] xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <!-- <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Create a new account
          </h1> -->
          <form class="space-y-2 md:space-y-4" @submit.prevent="handleSubmit">
            <div class="grid md:grid-cols-2 gap-[1rem]">
              <div>
                <label
                  for="email"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Your email</label
                >
                <input
                  v-model="form.email"
                  type="email"
                  name="email"
                  id="email"
                  class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="name@company.com"
                  required="" />
              </div>
              <div>
                <label
                  for="username"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Your username</label
                >
                <input
                  v-model="form.username"
                  type="text"
                  name="username"
                  id="username"
                  class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="username"
                  required="" />
              </div>
            </div>
            <div>
              <label
                for="bio"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your bio</label
              >
              <textarea
                id="bio"
                v-model="form.bio"
                name="bio"
                rows="4"
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Write your thoughts here..."></textarea>
            </div>

            <div class="grid grid-cols-2 gap-[1rem]">
              <div>
                <label
                  for="password"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Password</label
                >
                <input
                  v-model="form.password"
                  type="password"
                  name="password"
                  id="password"
                  placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  required="" />
              </div>
              <div>
                <label
                  for="password2"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Confirm Password</label
                >
                <input
                  v-model="form.password2"
                  type="password"
                  name="password2"
                  id="password2"
                  placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  required="" />
              </div>
            </div>

            <div>
              <label
                for="profile_picture"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Profile Picture</label
              >
              <input
                type="file"
                name="profile_picture"
                id="profile_picture"
                class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required="" />
            </div>
            <button
              type="submit"
              class="w-full text-white bg-primary hover:bg-primary-dark focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
              Sign Up
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Already have an account yet?
              <RouterLink
                to="sign-up"
                class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                >Sign in</RouterLink
              >
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
