<script setup>
import PulseLoader from "vue-spinner/src/PulseLoader.vue";
import BackButton from "@/components/BackButton.vue";
import { reactive, onMounted, computed } from "vue";
import { useRoute, RouterLink, useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const toast = useToast();

const taskId = route.params.id;

const state = reactive({
  task: {},
  isLoading: true,
});

const statusData = computed(() => {
  let temp = {
    label: "Pending",
    color: "#B8860B",
  };
  if (state.task?.status === "in_progress") {
    temp = {
      label: "In Progress",
      color: "blue",
    };
  } else if (state.task?.status === "completed") {
    temp = {
      label: "Completed",
      color: "green",
    };
  }
  return temp;
});

const deleteTask = async () => {
  try {
    const confirm = window.confirm(
      "Are you sure you want to delete this task?"
    );
    if (confirm) {
      await axios.delete(`/api/task/${taskId}/`);
      toast.success("Task Deleted Successfully");
      router.push("/tasks");
    }
  } catch (error) {
    console.error("Error deleting task", error);
    toast.error("Task Not Deleted");
  }
};

onMounted(async () => {
  try {
    const response = await axios.get(`/api/task/${taskId}`);
    state.task = response.data;
  } catch (error) {
    console.error("Error fetching task", error);
  } finally {
    state.isLoading = false;
  }
});
</script>

<template>
  <BackButton />
  <section v-if="!state.isLoading" class="bg-gray-50">
    <div class="container m-auto py-10 px-6">
      <div class="grid grid-cols-1 md:grid-cols-70/30 w-full gap-6">
        <main>
          <div
            class="bg-white p-6 rounded-lg shadow-md text-center md:text-left">
            <div
              :style="`color:${statusData.color}; border:1px solid ${statusData.color}`"
              class="text-gray-600 my-2 border text-center rounded-full max-w-[110px] py-1 mb-6">
              {{ statusData.label }}
            </div>
            <h1 class="text-3xl font-bold mb-4">{{ state.task.title }}</h1>
            <div
              class="text-gray-500 mb-4 flex align-middle justify-center md:justify-start">
              <i class="pi pi-calendar text-xl text-orange-700 mr-2"></i>
              <p class="text-orange-700">{{ state.task.due_date }}</p>
            </div>
          </div>

          <div class="bg-white p-6 rounded-lg shadow-md mt-6">
            <h3 class="text-primary-extra-dark text-lg font-bold mb-6">
              Task Description
            </h3>

            <p class="mb-4">
              {{ state.task.description }}
            </p>
          </div>
        </main>

        <!-- Sidebar -->
        <aside>
          <!-- Company Info -->
          <div class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold mb-6">Assignees</h3>

            <h2 class="text-2xl">{{ state.task.assigned_to }}</h2>
          </div>

          <!-- Manage -->
          <div class="bg-white p-6 rounded-lg shadow-md mt-6">
            <h3 class="text-xl font-bold mb-6">Manage task</h3>
            <RouterLink
              :to="`/tasks/edit/${state.task.id}`"
              class="bg-transparent hover:bg-primary-dark hover:text-white text-primary-dark text-center font-semibold py-2 px-4 rounded-lg w-full focus:outline-none focus:shadow-outline mt-4 block border border-primary-dark"
              >Edit task</RouterLink
            >
            <button
              @click="deleteTask"
              class="bg-transparent hover:bg-red-600 text-red-600 hover:text-white border border-red-600 font-semibold py-2 px-4 rounded-lg w-full focus:outline-none focus:shadow-outline mt-4 block">
              Delete task
            </button>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <div v-else class="text-center text-gray-500 py-6">
    <PulseLoader color="blue" />
  </div>
</template>
