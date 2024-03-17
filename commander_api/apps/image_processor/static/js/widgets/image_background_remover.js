import { ImageFileUpload } from "/static/js/widgets/image_file_upload.js";
export { ImageBackgroundRemover };

class ImageBackgroundRemover extends ImageFileUpload {
  constructor({ element, form }) {
    super({ element });
    this.form = form;
    this.image = this.container.querySelector(".loaded-image .widget-image");
    this.image_modified = this.container.querySelector(
      ".modified-image .widget-image"
    );
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
    this.image_modified.src = file;
  }
  submitForm() {
    console.log("Removing image background...");
    console.log(`${this.form} Removing image background...`);
    this.form.submit();
    // const formdata = new FormData(this.form);

    // fetch("/", {
    //   method: "POST",
    //   body: formdata,
    // })
    //   .then((response) => response.json())
    //   .catch((error) => console.error("Error:", error))
    //   .then((response) => console.log("Success:", response));
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
