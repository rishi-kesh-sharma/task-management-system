<script setup>
import { RouterLink } from "vue-router";
import { defineProps, ref, computed, onMounted, reactive } from "vue";

const props = defineProps({
  task: Object,
});

const statusData = computed(() => {
  let temp = {
    label: "Pending",
    color: "#B8860B",
  };
  if (props.task?.status === "in_progress") {
    temp = {
      label: "In Progress",
      color: "blue",
    };
  } else if (props.task?.status === "completed") {
    temp = {
      label: "Completed",
      color: "green",
    };
  }
  return temp;
});

const showFullDescription = ref(false);

const toggleFullDescription = () => {
  showFullDescription.value = !showFullDescription.value;
};

const truncatedDescription = computed(() => {
  let description = props.task.description;
  if (!showFullDescription.value) {
    description = description.substring(0, 90) + "...";
  }
  return description;
});
</script>

<template>
  <div class="bg-white rounded-xl shadow-md relative">
    <div class="p-4">
      <div class="mb-2">
        <div
          :style="`color:${statusData.color}; border:1px solid ${statusData.color}`"
          class="text-gray-600 my-2 border text-center rounded-full max-w-[110px] py-1 mb-6">
          {{ statusData.label }}
        </div>
        <h3 class="text-xl font-bold">{{ task.title }}</h3>
      </div>

      <div class="mb-5">
        <div class="text-gray-600">
          {{ truncatedDescription }}
        </div>
        <button
          @click="toggleFullDescription"
          class="text-primary hover:text-primary mb-5">
          {{ showFullDescription ? "less" : "more" }}
        </button>
      </div>

      <div class="border border-gray-100 mb-5"></div>

      <div class="flex flex-col lg:flex-row justify-between mb-1">
        <h3 class="text-primary mb-2">{{ task.assigned_to }}</h3>
        <RouterLink
          :to="'/tasks/' + task.id"
          class="h-[36px] bg-transparent hover:bg-primary-dark text-primary border border-primary max-w-[110px] px-4 py-2 rounded-lg text-center text-sm hover:text-white">
          Read More
        </RouterLink>
      </div>
    </div>
  </div>
</template>
