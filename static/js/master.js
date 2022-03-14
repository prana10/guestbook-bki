/******
 *
 * Jquery Function for Validated and Read name file for input file
 */

"use strict";

$(function () {
  $(".my-login-validation").submit(function () {
    var form = $(this);
    if (form[0].checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
    }
    form.addClass("was-validated");
  });
});
const realFileBtn = document.getElementById("real-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");

customBtn.addEventListener("click", function () {
  realFileBtn.click();
});

realFileBtn.addEventListener("change", function () {
  if (realFileBtn.value) {
    customTxt.innerHTML =
      `<i class="uil uil-images"></i> ` +
      realFileBtn.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
  } else {
    customTxt.innerHTML = `<i class="uil uil-camera"></i> Open Your Camera`;
  }
});
