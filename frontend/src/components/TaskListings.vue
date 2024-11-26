<script setup>
import { RouterLink } from "vue-router";
import TaskListing from "./TaskListing.vue";
import { reactive, defineProps, onMounted } from "vue";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";
import axios from "axios";

defineProps({
  limit: Number,
  showButton: {
    type: Boolean,
    default: false,
  },
});

const state = reactive({
  tasks: [],
  isLoading: true,
});

onMounted(async () => {
  try {
    const response = await axios.get("/api/task/");
    state.tasks = response.data;
  } catch (error) {
    console.error("Error fetching tasks", error);
  } finally {
    state.isLoading = false;
  }
});
</script>

<template>
  <section class="bg-blue-50 px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-bold text-primary mb-6 text-center">
        Browse tasks
      </h2>
      <!-- Show loading spinner while loading is true -->
      <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
        <PulseLoader />
      </div>

      <!-- Shoe task listing when done loading -->
      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <taskListing
          v-for="task in state.tasks.slice(0, limit || state.tasks.length)"
          :key="task.id"
          :task="task" />
      </div>
    </div>
  </section>

  <section v-if="showButton" class="m-auto max-w-lg my-10 px-6">
    <RouterLink
      to="/tasks"
      class="block bg-black text-white text-center py-4 px-6 rounded-xl hover:bg-gray-700"
      >View All tasks</RouterLink
    >
  </section>
</template>
