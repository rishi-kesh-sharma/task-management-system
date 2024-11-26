<script setup>
import { RouterLink } from "vue-router";
import Card from "@/components/Card.vue";
</script>

<template>
  <section class="py-4">
    <div class="container-xl lg:container m-auto">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 rounded-lg">
        <Card>
          <h2 class="text-2xl font-bold">Tasks</h2>
          <p class="mt-2 mb-4">
            Browse your tasks and start managing with ease
          </p>
          <RouterLink
            to="/tasks"
            class="inline-block bg-black text-white rounded-lg px-4 py-2 hover:bg-gray-700">
            Browse tasks
          </RouterLink>
        </Card>
        <Card bg="bg-primary-extra-light">
          <h2 class="text-2xl font-bold">Profiling</h2>
          <p class="mt-2 mb-4">Organize Tasks and Manage Profile Seamlessly!</p>
          <RouterLink
            to="/tasks/add"
            class="inline-block bg-primary text-white rounded-lg px-4 py-2 hover:bg-primary">
            Add task
          </RouterLink>
        </Card>
      </div>
    </div>
  </section>
</template>
