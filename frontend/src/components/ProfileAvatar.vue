<script setup>
import { RouterLink, useRouter } from "vue-router";
import Logo from "@/assets/img/logo.png";
const user = JSON.parse(localStorage.getItem("user"));
const router = useRouter();
const handleLogout = async () => {
  // const response = await axios.get
  localStorage.clear();
  window.location.href = "/login";
};
</script>

<template>
  <img
    id="avatarButton"
    type="button"
    data-dropdown-toggle="userDropdown"
    data-dropdown-placement="bottom-start"
    class="w-10 h-10 rounded-full cursor-pointer"
    :src="user.profile_picture || Logo"
    alt="User dropdown" />

  <!-- Dropdown menu -->
  <div
    id="userDropdown"
    class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
    <div class="px-4 py-3 text-sm text-gray-900 dark:text-white">
      <div>{{ user.username }}</div>
      <div class="font-medium truncate">{{ user.email }}</div>
    </div>
    <ul
      class="py-2 text-sm text-gray-700 dark:text-gray-200"
      aria-labelledby="avatarButton">
      <li>
        <RouterLink
          to="/profile"
          class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
          >Profile</RouterLink
        >
      </li>
      <li>
        <RouterLink
          to="/tasks"
          class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
          >Tasks</RouterLink
        >
      </li>
    </ul>
    <div class="py-1">
      <button
        @click="handleLogout"
        class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white w-full flex justify-self-start">
        Sign out
      </button>
    </div>
  </div>
</template>
