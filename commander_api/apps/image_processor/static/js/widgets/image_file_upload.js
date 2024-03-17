export { ImageFileUpload };
class ImageFileUpload {
  constructor({ element }) {
    this.container = element;
    this.image = this.container.querySelector(".widget-image");
    this.input = this.container.querySelector(".widget-input");
    this.label = this.container.querySelector(".widget-label");
  }

  highlight() {
    this.container.classList.add("highlight");
  }
  unhighlight() {
    this.container.classList.remove("highlight");
  }

  handleFile(file) {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = () => {
      this.previewFile(reader.result);
      this.submitForm();
    };
  }
  handleFilesDropped(event) {
    const dt = event.dataTransfer;
    const [file] = dt.files;
    this.handleFile(file);
  }
  handleFilesInput(event) {
    const [file] = this.input.files;
    this.handleFile(file);
  }

  previewFile(file) {
    this.image.src = file;
  }

  load() {
    ["dragenter", "dragover", "dragleave", "drop"].forEach((ev) => {
      this.container.addEventListener(
        ev,
        (e) => {
          e.preventDefault();
          e.stopPropagation();
        },
        false
      );
    });
    ["dragenter", "dragover"].forEach((ev) => {
      this.container.addEventListener(ev, this.highlight.bind(this), false);
    });
    ["dragleave", "drop"].forEach((ev) => {
      this.container.addEventListener(ev, this.unhighlight.bind(this), false);
    });
    this.container.addEventListener(
      "drop",
      this.handleFilesDropped.bind(this),
      false
    );
    this.container.addEventListener(
      "change",
      this.handleFilesInput.bind(this),
      false
    );
  }
}

document.querySelectorAll(".image-upload-widget").forEach((widget) => {
  const img_bg_remover = new ImageFileUpload({ element: widget });
  img_bg_remover.load();
});
