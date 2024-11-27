<script>
const cloudName = "dvtaczewf"; // replace with your own cloud name
const uploadPreset = "task-management-system"; // replace with your own upload preset
import axios from "axios";

const myWidget = cloudinary.createUploadWidget(
  {
    cloudName: cloudName,
    uploadPreset: uploadPreset,
    // cropping: true, //add a cropping step
    // showAdvancedOptions: true,  //add advanced options (public_id and tag)
    // sources: [ "local", "url"], // restrict the upload sources to URL and local files
    // multiple: false,  //restrict upload to a single file
    // folder: "user_images", //upload files to the specified folder
    // tags: ["users", "profile"], //add the given tags to the uploaded files
    // context: {alt: "user_uploaded"}, //add the given context data to the uploaded files
    // clientAllowedFormats: ["images"], //restrict uploading to image files only
    // maxImageFileSize: 2000000,  //restrict file size to less than 2MB
    // maxImageWidth: 2000, //Scales the image down to a width of 2000 pixels before uploading
    // theme: "purple", //change to a purple theme
  },

  async (error, result) => {
    if (!error && result && result.event === "success") {
      console.log("Done! Here is the image info: ", result.info);
      //   profile_picture_url = result.info.secure_url;
      document.getElementById(
        "uploaded_image"
      ).style.background = `url(${result.info.secure_url})`;

      try {
        const response = await axios.put(
          "/api/user/profile/upload/",
          {
            profile_picture: result.info.secure_url,
          },
          {
            headers: {
              Authorization: `Bearer ${
                JSON.parse(localStorage.getItem("token")).access
              }`,
            },
          }
        );

        const data = response.data;
      } catch (err) {
        console.log(err);
      }
      try {
        const profileResponse = await axios.get(`/api/user/profile`, {
          headers: {
            Authorization: `Bearer ${
              JSON.parse(localStorage.getItem("token")).access
            }`,
          },
        });

        // clear localstorage item user
        localStorage.removeItem("user");
        const profileData = JSON.stringify(profileResponse.data);

        // set user to localstorage
        localStorage.setItem("user", profileData);
        window.location.href = "/profile";
      } catch (err) {
        console.log(err);
      }
    }
  }
);

export default {
  name: "UploadWidget",
  data: () => ({
    open: function () {
      myWidget.open();
    },
    profile_picture_url: "",
  }),
  props: {
    trigger: Element,
    image_url: String,
  },
};
</script>

<template>
  <div
    class="uw absolute left-[50%] top-[50%] translate-x-[-50%] translate-y-[-50%]">
    <button
      v-on:click="open"
      id="upload_widget"
      class=""
      role="button"
      type="button">
      <div
        id="uploaded_image"
        :style="`background:url(${profile_picture_url || image_url});`"
        :class="`mx-auto flex justify-center w-[141px] h-[141px] rounded-full bg-contain  bg-no-repeat`">
        <div class="bg-white/90 rounded-full w-6 h-6 text-center ml-28 mt-4">
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
    </button>
  </div>
</template>
