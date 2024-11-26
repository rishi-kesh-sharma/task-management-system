<script setup>
import { defineProps } from "vue";

defineProps({
  title: {
    type: String,
    default: "Your Go To Task Manager",
  },
  subtitle: {
    type: String,
    default: "Effortless Task Management: Create, Update, and Stay Organized!",
  },
});
</script>

<template>
  <section
    class="bg-cover min-h-[49vh] bg-no-repeat py-20 bg-[url('https://images.unsplash.com/photo-1466853817435-05b43fe45b39?q=80&w=1999&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')]">
    <div
      class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center">
      <div class="text-center">
        <h1 class="text-3xl font-bold text-white sm:text-5xl md:text-6xl">
          {{ title }}
        </h1>
        <p class="my-4 text-lg text-white">
          {{ subtitle }}
        </p>
      </div>
    </div>
  </section>
</template>
