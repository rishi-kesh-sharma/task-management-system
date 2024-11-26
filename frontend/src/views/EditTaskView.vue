<script setup>
import router from "@/router";
import { reactive, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useToast } from "vue-toastification";
import axios from "axios";

const route = useRoute();

const taskId = route.params.id;

const form = reactive({
  title: "",
  description: "",
  status: "",
  due_date: "",
  assigned_to: "",
});

const state = reactive({
  task: {},
  isLoading: true,
});

const toast = useToast();

const handleSubmit = async () => {
  const updatedTask = {
    title: form.title,
    description: form.description,
    status: form.status,
    due_date: form.due_date,
    assigned_to: form.assigned_to,
  };

  try {
    const response = await axios.put(`/api/tasks/${taskId}`, updatedTask);
    toast.success("task Updated Successfully");
    router.push(`/tasks/${response.data.id}`);
  } catch (error) {
    console.error("Error fetching task", error);
    toast.error("task Was Not Added");
  }
};

onMounted(async () => {
  try {
    const response = await axios.get(`/api/tasks/${taskId}`);
    state.task = response.data;
    // Populate inputs
    form.title = state.task.title;
    form.description = state.task.description;
    form.status = state.task.status;
    form.due_date = state.task.due_date;
    form.assigned_to = state.task.assigned_to;
  } catch (error) {
    console.error("Error fetching task", error);
  } finally {
    state.isLoading = false;
  }
});
</script>

<template>
  <section class="bg-primary-extra-light">
    <div class="container m-auto max-w-2xl py-24">
      <div
        class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
        <form @submit.prevent="handleSubmit">
          <h2 class="text-3xl text-center font-semibold mb-6">Update task</h2>

          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2">Task Title</label>
            <input
              type="text"
              v-model="form.title"
              id="title"
              name="title"
              class="border rounded w-full py-2 px-3 mb-2"
              placeholder="eg. Create beautiful and intuitive UI"
              required />
          </div>
          <div class="mb-4">
            <label for="description" class="block text-gray-700 font-bold mb-2"
              >Description</label
            >
            <textarea
              id="description"
              v-model="form.description"
              name="description"
              class="border rounded w-full py-2 px-3"
              rows="4"
              placeholder="Add any task duties, expectations, requirements, etc"></textarea>
          </div>

          <div class="mb-4">
            <label for="type" class="block text-gray-700 font-bold mb-2"
              >Status</label
            >
            <select
              id="status"
              v-model="form.status"
              name="status"
              class="border rounded w-full py-2 px-3"
              required>
              <option value="Pending">Pending</option>
              <option value="In Progress">In Progress</option>
              <option value="Completed">Completed</option>
            </select>
          </div>

          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2"> Due Date </label>
            <input
              type="date"
              v-model="form.due_date"
              id="due_date"
              name="due_date"
              class="border rounded w-full py-2 px-3 mb-2"
              placeholder="Task due date"
              required />
          </div>

          <div class="mb-4">
            <label for="company" class="block text-gray-700 font-bold mb-2"
              >Assigned_to</label
            >
            <input
              type="text"
              v-model="form.assigned_to"
              id="assigned_to"
              name="assigned_to"
              class="border rounded w-full py-2 px-3"
              placeholder="Assignee's Name" />
          </div>

          <div>
            <button
              class="bg-primary hover:bg-primary text-white font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline"
              type="submit">
              Update Task
            </button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>
