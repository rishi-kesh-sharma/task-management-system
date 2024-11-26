import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import tasksView from "@/views/TasksView.vue";
import NotFoundView from "@/views/NotFoundView.vue";
import TaskView from "@/views/TaskView.vue";
import AddTaskView from "@/views/AddTaskView.vue";
import EditTaskView from "@/views/EditTaskView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/tasks",
      name: "tasks",
      component: tasksView,
    },
    {
      path: "/tasks/:id",
      name: "task",
      component: TaskView,
    },
    {
      path: "/tasks/add",
      name: "add-task",
      component: AddTaskView,
    },
    {
      path: "/tasks/edit/:id",
      name: "edit-task",
      component: EditTaskView,
    },
    {
      path: "/:catchAll(.*)",
      name: "not-found",
      component: NotFoundView,
    },
  ],
});

export default router;
