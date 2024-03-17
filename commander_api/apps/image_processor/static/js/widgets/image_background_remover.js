class ImageBackgroundRemover {
  constructor({ element }) {
    this.container = element;
    this.image = this.container.querySelector(".background-remover-image");
    this.input = this.container.querySelector(".background-remover-input");
    this.label = this.container.querySelector(".background-remover-label");
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
      this.uploadFile(reader.result);
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

  uploadFile(file) {
    console.log("work in progress...");
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

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".background-remover-widget").forEach((widget) => {
    const img_bg_remover = new ImageBackgroundRemover({ element: widget });
    img_bg_remover.load();
  });
});
