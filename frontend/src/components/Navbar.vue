<script setup>
import { RouterLink, useRoute } from "vue-router";
import logo from "@/assets/img/logo.png";
import ProfileAvatar from "@/components/ProfileAvatar.vue";

const profileData = JSON.parse(localStorage.getItem("user"));
const isAuthenticated = localStorage.getItem("isAuthenticated");

const isActiveLink = (routePath) => {
  const route = useRoute();
  return route.path === routePath;
};
</script>

<template>
  <nav class="bg-primary-dark border-b border-primary-extra-dark">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <div
          class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <!-- Logo -->
          <RouterLink class="flex flex-shrink-0 items-center mr-4" to="/">
            <img class="h-10 w-auto" :src="logo" alt="Taskify" />
            <span class="hidden md:block text-white text-2xl font-bold ml-2"
              >Taskify</span
            >
          </RouterLink>
          <div class="md:ml-auto">
            <div class="flex space-x-2">
              <RouterLink
                to="/"
                :class="[
                  isActiveLink('/')
                    ? 'bg-primary-extra-dark'
                    : 'hover:bg-primary-extra-dark hover:text-white',
                  'text-white',
                  'px-3',
                  'py-2',
                  'rounded-md',
                ]"
                >Home</RouterLink
              >
              <RouterLink
                to="/tasks"
                :class="[
                  isActiveLink('/tasks')
                    ? 'bg-primary-extra-dark'
                    : 'hover:bg-primary-extra-dark hover:text-white',
                  'text-white',
                  'px-3',
                  'py-2',
                  'rounded-md',
                ]"
                >Tasks</RouterLink
              >
              <RouterLink
                to="/tasks/add"
                :class="[
                  isActiveLink('/tasks/add')
                    ? 'bg-primary-extra-dark'
                    : 'hover:bg-primary-extra-dark hover:text-white',
                  'text-white',
                  'px-3',
                  'py-2',
                  'rounded-md',
                ]"
                >Add Task</RouterLink
              >
              <RouterLink
                v-if="!isAuthenticated"
                to="/login"
                :class="[
                  isActiveLink('/login')
                    ? 'bg-primary-extra-dark'
                    : 'hover:bg-primary-extra-dark hover:text-white',
                  'text-white',
                  'px-3',
                  'py-2',
                  'rounded-md',
                ]"
                >Login</RouterLink
              >
              <ProfileAvatar v-else />
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
