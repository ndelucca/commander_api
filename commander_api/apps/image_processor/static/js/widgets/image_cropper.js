import { ImageFileUpload } from "/static/js/widgets/image_file_upload.js";
export { ImageCropperWidget };

class ImageCropperWidget extends ImageFileUpload {
  constructor({ element }) {
    super({ element });
  }
}

document.querySelectorAll(".image_cropper-widget").forEach((widget) => {
  const img_cropper = new ImageCropperWidget({
    element: widget,
    form: form,
  });
  img_cropper.load();
});
