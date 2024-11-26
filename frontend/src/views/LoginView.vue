<script setup>
import { RouterLink, useRouter } from "vue-router";
import Logo from "@/assets/img/logo.png";
import { reactive } from "vue";
import axios from "axios";

const router = useRouter();

const form = reactive({
  email: "",
  password: "",
});

const handleSubmit = async () => {
  const body = {
    email: form.email,
    password: form.password,
  };
  const response = await axios.post(`/api/user/login/`, body);
  const data = response.data;
  const profileResponse = await axios.get(`/api/user/profile`, {
    headers: {
      Authorization: `Bearer ${data.token.access}`,
    },
  });

  // clear localstorage
  localStorage.clear();
  const token = JSON.stringify(data.token);
  const profileData = JSON.stringify(profileResponse.data);

  // set the items to localstorage
  localStorage.setItem("token", token);
  localStorage.setItem("user", profileData);
  localStorage.setItem("isAuthenticated", true);
  window.location.href = "/";
};
</script>

<template>
  <section class="bg-gray-50 dark:bg-gray-900 pt-[2rem]">
    <div
      class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:max-h-screen lg:py-0">
      <RouterLink
        to="/"
        class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
        <img class="w-8 h-8 mr-2" :src="Logo" alt="logo" />
        Vue Task
      </RouterLink>
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Sign in to your account
          </h1>
          <form class="space-y-4 md:space-y-6" @submit.prevent="handleSubmit">
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
            <div class="flex items-center justify-end">
              <RouterLink
                to="/forgot-password"
                class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"
                >Forgot password?</RouterLink
              >
            </div>
            <button
              type="submit"
              class="w-full text-white bg-primary hover:bg-primary-dark focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
              Sign in
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Don’t have an account yet?
              <RouterLink
                to="signup"
                class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                >Sign up</RouterLink
              >
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
