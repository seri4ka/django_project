document.addEventListener("DOMContentLoaded", function () {
  // Проверка видимости элемента
  function isInViewport(element) {
      const rect = element.getBoundingClientRect();
      return (
          rect.top >= 0 &&
          rect.left >= 0 &&
          rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
          rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
  }

  // // Функция для отображения элементов
  // function revealElement(element) {
  //     element.classList.add("reveal");
  // }

  // Найти скрытые элементы
  // const hiddenElements = document.querySelectorAll(".hidden");

  // // Событие прокрутки
  // window.addEventListener("scroll", function () {
  //     hiddenElements.forEach((element) => {
  //         if (isInViewport(element)) {
  //             revealElement(element);
  //         }
  //     });
  // });

  // Установка начального состояния для скрытых элементов
  hiddenElements.forEach((element) => {
      element.classList.add("initial-hidden");
  });
});
