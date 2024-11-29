<script setup>
import { onMounted, reactive, defineProps } from "vue";
import Avatar from "@/components/Avatar.vue";

const props = defineProps([
  "filters",
  "assignees",
  "setFilters",
  "resetFilters",
]);
const state = reactive({
  form: {
    status: props.filters.status,
    assigned_to: props.filters.assigned_to,
  },
});

const handleSubmit = async () => {
  console.log(state.form);

  //  props
  props.setFilters(state.form);
};

const handleReset = async () => {
  console.log(state.form);
  props.resetFilters();
};
</script>

<template>
  <details
    open
    class="w-full mt-10 overflow-hidden rounded-lg border border-gray-200 open:shadow-lg text-gray-700 container-xl lg:container m-auto">
    <summary
      class="flex cursor-pointer select-none items-center justify-between bg-gray-100 py-3 px-5">
      <span class="text-sm font-medium"> Task Filters </span>

      <svg
        class="h-5 w-5"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M4 6h16M4 12h16M4 18h16" />
      </svg>
    </summary>

    <form @submit.prevent="handleSubmit">
      <div class="flex border-t border-gray-200 lg:border-t-0 px-5 gap-12">
        <fieldset class="w-full pb-4">
          <legend class="block w-full py-3 text-xs font-bold">Status</legend>

          <div class="flex gap-4 justify-between items-center">
            <div class="flex gap-4 items-center">
              <div class="flex items-center">
                <input
                  v-model="state.form.status"
                  :checked="state.form.status === 'pending'"
                  id="pending"
                  type="radio"
                  name="status"
                  value="pending"
                  class="h-5 w-5 rounded border-gray-300" />

                <label for="300+" class="ml-1 text-sm font-medium">
                  Pending</label
                >
              </div>

              <div class="flex items-center">
                <input
                  v-model="state.form.status"
                  :checked="state.form.status === 'in_progress'"
                  id="in_progress"
                  type="radio"
                  name="status"
                  value="in_progress"
                  class="h-5 w-5 rounded border-gray-300" />

                <label for="600+" class="ml-1 text-sm font-medium">
                  In Progress
                </label>
              </div>

              <div class="flex items-center">
                <input
                  v-model="state.form.status"
                  :checked="state.form.status === 'completed'"
                  id="completed"
                  type="radio"
                  name="status"
                  value="completed"
                  class="h-5 w-5 rounded border-gray-300" />

                <label for="1500+" class="ml-1 text-sm font-medium">
                  Completed
                </label>
              </div>
            </div>
            <div class="">
              <button
                type="button"
                class="text-xs bg-transparent border border-primary p-2 rounded-full text-primary">
                Reset Type
              </button>
            </div>
          </div>
        </fieldset>
        <fieldset class="w-full pb-4">
          <legend class="block w-full bg-gray-50 py-3 text-xs font-bold">
            Assigned To
          </legend>

          <div class="flex gap-4 justify-between items-center">
            <div class="flex gap-4 items-center">
              <div
                v-for="assignee in assignees"
                :key="assignee.id"
                class="flex items-center">
                <input
                  v-model="state.form.assigned_to"
                  :checked="state.form.assigned_to == assignee.id"
                  :id="assignee.id"
                  type="radio"
                  name="assigned_to"
                  :value="assignee.id"
                  class="h-5 w-5 rounded border-gray-300" />

                <label for="300+" class="ml-1 text-sm font-medium">
                  <div>
                    <div
                      :id="assignee.username"
                      role="tooltip"
                      class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 shadow-sm opacity-0 tooltip dark:bg-gray-700">
                      {{ assignee.username }}
                      <div class="tooltip-arrow" data-popper-arrow></div>
                    </div>
                    <img
                      :data-tooltip-target="assignee.username"
                      class="w-10 h-10 rounded-full"
                      :src="assignee.profile_picture"
                      alt="Medium avatar" />
                  </div>

                  <!-- <Avatar :user="assignee" :key="assignee.id" /> -->
                </label>
              </div>
            </div>
            <div class="">
              <button
                type="button"
                class="text-xs bg-transparent border border-primary p-2 rounded-full text-primary">
                Reset Type
              </button>
            </div>
          </div>
        </fieldset>
      </div>
      <div class="">
        <div class="flex justify-between border-t border-gray-200 px-5 py-3">
          <button
            @click="handleReset"
            type="button"
            class="text-xs bg-transparent border border-primary p-2 rounded-full text-primary">
            Reset All
          </button>

          <button
            @click="handleSubmit"
            name="commit"
            type="submit"
            class="rounded-full bg-blue-600 px-5 py-3 text-xs font-medium text-white active:scale-95">
            Apply Filters
          </button>
        </div>
      </div>
    </form>
  </details>
</template>
