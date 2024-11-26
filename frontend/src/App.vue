<script setup>
import Navbar from "@/components/Navbar.vue";
import { RouterView } from "vue-router";

const isAuthenticated = localStorage.getItem("isAuthenticated");
</script>

<template>
  <Navbar v-if="isAuthenticated" />
  <RouterView />
</template>
