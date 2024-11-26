import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import tasksView from "@/views/TasksView.vue";
import NotFoundView from "@/views/NotFoundView.vue";
import TaskView from "@/views/TaskView.vue";
import AddTaskView from "@/views/AddTaskView.vue";
import EditTaskView from "@/views/EditTaskView.vue";
import LoginView from "@/views/LoginView.vue";
import SignupView from "@/views/SignupView.vue";
import UpdateProfileView from "@/views/UpdateProfileView.vue";
import ForgotPasswordView from "@/views/ForgotPasswordView.vue";
import ResetPasswordView from "@/views/ResetPasswordView.vue";
import ProfileView from "@/views/ProfileView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/forgot-password",
      name: "forgot password",
      component: ForgotPasswordView,
    },
    {
      path: "/reset-password",
      name: "reset password",
      component: ResetPasswordView,
    },
    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
    },
    {
      path: "/profile/update",
      name: "update profile",
      component: UpdateProfileView,
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

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem("isAuthenticated");
  if (
    !isAuthenticated &&
    (to.name === "signup" ||
      to.name === "forgot password" ||
      to.name === "reset password")
  ) {
    next();
  }
  if (to.name !== "login" && !isAuthenticated) next({ name: "login" });
  // else if (to.name !== "signup" && !isAuthenticated) next({ name: "signup" });
  else next();
});

export default router;
