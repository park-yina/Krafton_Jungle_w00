export default class Cards {
  constructor(array) {
    this.src = array;
    console.log(this.src);
    this.imgTestDiv = document.querySelector("#imgTest");
  }

  create() {
    this.src.forEach((element) => {
      const img = document.createElement("img");
      img.src = `data:image/png;base64,${element.img_src}`;
      this.imgTestDiv.append(img);
    });
  }
}
