<script setup>
import { RouterLink } from "vue-router";
const user = JSON.parse(localStorage.getItem("user"));
</script>

<template>
  <section class="my-auto dark:bg-gray-900">
    <div class="lg:w-[80%] md:w-[90%] xs:w-[96%] mx-auto flex gap-4">
      <div
        class="lg:w-[88%] md:w-[80%] sm:w-[88%] xs:w-full mx-auto shadow-2xl p-5 rounded-xl h-fit self-center dark:bg-gray-800/40">
        <form>
          <div
            class="relative w-full rounded-sm min-h-[30vh] bg-[url('https://images.unsplash.com/photo-1449844908441-8829872d2607?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NzEyNjZ8MHwxfHNlYXJjaHw2fHxob21lfGVufDB8MHx8fDE3MTA0MDE1NDZ8MA&ixlib=rb-4.0.3&q=80&w=1080')] bg-cover bg-center bg-no-repeat flex items-center">
            <!-- Profile Image -->
            <RouterLink
              to="/profile/update"
              class="absolute h-10 w-10 z-100 bg-gray-200 rounded-full top-0 right-0 flex items-center justify-center cursor-pointer m-2">
              <i class="pi pi-user-edit text-primary-dark text-2xl"></i>
            </RouterLink>
            <div
              :style="`background:url(${user.profile_picture})`"
              :class="`mx-auto flex justify-center items-center w-[141px] h-[141px] bg-blue-300/20 rounded-full  bg-cover bg-center bg-no-repeat`">
              <div
                class="bg-white/90 rounded-full w-6 h-6 text-center ml-28 mt-4">
                <input
                  value="user.profile_picture"
                  type="file"
                  name="profile_picture"
                  disabled
                  id="profile_picture"
                  hidden
                  required />

                <label for="profile_picture">
                  <svg
                    data-slot="icon"
                    class="w-6 h-5 text-blue-700"
                    fill="none"
                    stroke-width="1.5"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                    aria-hidden="true">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M6.827 6.175A2.31 2.31 0 0 1 5.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 0 0-1.134-.175 2.31 2.31 0 0 1-1.64-1.055l-.822-1.316a2.192 2.192 0 0 0-1.736-1.039 48.774 48.774 0 0 0-5.232 0 2.192 2.192 0 0 0-1.736 1.039l-.821 1.316Z"></path>
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M16.5 12.75a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0ZM18.75 10.5h.008v.008h-.008V10.5Z"></path>
                  </svg>
                </label>
              </div>
            </div>
          </div>
          <div
            class="flex lg:flex-row md:flex-col sm:flex-col xs:flex-col gap-x-[2rem] justify-center w-full">
            <div class="w-full mb-4 mt-6">
              <label for="email" class="mb-2 dark:text-gray-300"> Email</label>
              <input
                type="email"
                name="email"
                disabled
                :value="user.email"
                id="email"
                class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800"
                placeholder="name@company.com" />
            </div>
            <div class="w-full mb-4 lg:mt-6">
              <label for="username" class="dark:text-gray-300"> Username</label>
              <input
                type="text"
                name="username"
                disabled
                id="username"
                :value="user.username"
                class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800"
                placeholder="Username" />
            </div>
          </div>

          <div class="w-full mb-4 lg:mt-2">
            <label
              for="bio"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Your bio</label
            >
            <textarea
              id="bio"
              name="bio"
              disabled
              :value="user.bio"
              rows="6"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Your bio here..."></textarea>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>
