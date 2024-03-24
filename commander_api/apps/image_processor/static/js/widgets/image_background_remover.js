import { ImageFileUpload } from "/static/js/widgets/image_file_upload.js";
export { ImageBackgroundRemover };

class ImageBackgroundRemover extends ImageFileUpload {
  constructor({ element, form }) {
    super({ element });
    this.form = form;
    this.loaded_image = this.container.querySelector(".loaded-image");
    this.image = this.loaded_image.querySelector(".widget-image");
    this.image_modified = this.container.querySelector(
      ".modified-image .widget-image"
    );
    this.image_modified_link = this.container.querySelector(
      ".modified-image-link"
    );
  }
  highlight() {
    this.loaded_image.classList.add("highlight");
  }
  unhighlight() {
    this.loaded_image.classList.remove("highlight");
  }
  handleFile(file) {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = () => {
      this.previewFile(reader.result);
      this.submitForm();
    };
  }
  previewFile(file) {
    this.image.src = file;
  }
  submitForm() {
    this.image_modified.src = "/static/img/loading.svg";

    const formdata = new FormData(this.form);

    fetch("", {
      method: "POST",
      body: formdata,
    })
      .then((response) => response.json())
      .catch((error) => {
        this.image_modified.src = "";
        console.error("Error:", error);
      })
      .then((response) => {
        this.image_modified_link.download = "reduced_image.png";
        this.image_modified_link.href = response.image_file;
        this.image_modified.src = response.image_file;
      });
  }
}
for (const form of document.forms) {
  form.querySelectorAll(".background-remover-widget").forEach((widget) => {
    const img_bg_remover = new ImageBackgroundRemover({
      element: widget,
      form: form,
    });
    img_bg_remover.load();
  });
}
