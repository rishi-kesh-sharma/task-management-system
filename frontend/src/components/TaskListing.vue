<script setup>
import { RouterLink } from "vue-router";
import { defineProps, ref, computed } from "vue";

const props = defineProps({
  task: Object,
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
      <div class="mb-6">
        <div class="text-gray-600 my-2">{{ task.type }}</div>
        <h3 class="text-xl font-bold">{{ task.title }}</h3>
      </div>

      <div class="mb-5">
        <div>
          {{ truncatedDescription }}
        </div>
        <button
          @click="toggleFullDescription"
          class="text-primary hover:text-primary mb-5">
          {{ showFullDescription ? "Less" : "More" }}
        </button>
      </div>

      <h3 class="text-primary mb-2">{{ task.salary }} / Year</h3>

      <div class="border border-gray-100 mb-5"></div>

      <div class="flex flex-col lg:flex-row justify-between mb-4">
        <div class="text-orange-700 mb-3">
          <i class="pi pi-map-marker text-orange-700"></i>
          {{ task.location }}
        </div>
        <RouterLink
          :to="'/tasks/' + task.id"
          class="h-[36px] bg-primary hover:bg-primary text-white px-4 py-2 rounded-lg text-center text-sm">
          Read More
        </RouterLink>
      </div>
    </div>
  </div>
</template>
