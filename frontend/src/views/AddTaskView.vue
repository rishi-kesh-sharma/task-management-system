<script setup>
import router from "@/router";
import { reactive } from "vue";
import { useToast } from "vue-toastification";
import axios from "axios";

const form = reactive({
  title: "",
  description: "",
  // status: "",
  due_date: "",
  assigned_to: "",
});

const toast = useToast();

const handleSubmit = async () => {
  const newTask = {
    title: form.title,
    description: form.description,
    // status: form.status,
    due_date: form.due_date,
    assigned_to: form.assigned_to,
  };

  try {
    const response = await axios.post("/api/task/", newTask);
    toast.success("task Added Successfully");
    router.push(`/tasks/${response.data.id}`);
  } catch (error) {
    console.error("Error fetching task", error);
    toast.error("Task Was Not Added");
  }
};
</script>

<template>
  <section class="bg-gray-50">
    <div class="container m-auto max-w-[900px] py-5">
      <div
        class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
        <form @submit.prevent="handleSubmit">
          <h2 class="text-3xl text-center font-semibold mb-6">Add Task</h2>

          <div class="grid grid-cols-2 gap-[1rem]">
            <div class="mb-4 col-span-2">
              <label class="block text-gray-700 font-bold mb-2"
                >Task Title</label
              >
              <input
                type="text"
                v-model="form.title"
                id="title"
                name="title"
                class="border rounded w-full py-2 px-3 mb-2"
                placeholder="eg. Create beautiful and intuitive UI"
                required />
            </div>
          </div>

          <div class="grid grid-cols-2 gap-x-[1rem]">
            <div class="mb-4">
              <label class="block text-gray-700 font-bold mb-2">
                Due Date
              </label>
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

          <div>
            <button
              class="bg-primary hover:bg-primary-dark text-white font-bold py-3 px-4 rounded-lg w-full focus:outline-none focus:shadow-outline"
              type="submit">
              Add Task
            </button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>
