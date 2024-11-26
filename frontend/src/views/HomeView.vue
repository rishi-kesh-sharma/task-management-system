<script setup>
import Hero from "@/components/Hero.vue";
import HomeCards from "@/components/HomeCards.vue";
import TaskListings from "@/components/TaskListings.vue";
</script>

<template>
  <Hero />
  <HomeCards />
  <TaskListings :limit="3" :showButton="true" />
</template>
