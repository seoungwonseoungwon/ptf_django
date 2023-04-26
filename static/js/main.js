// nav높이 + container(contents) 높이 + footer 높이 < viewport 높이
//    :  footer 요소를 viewport 아래에 fixed
// nav높이 + container높이 + footer높이 >= viewport높이
//    :  footer 요소의 fixed 속성을 제거함
let nav_h = document.querySelector('.navbar').clientHeight;
let con_h = document.querySelector('div.contents').clientHeight;
let footer_h = document.querySelector('footer').clientHeight;
// navbar, container, footer 높이 콘솔 출력
console.log(nav_h, con_h, footer_h)
// viewport 높이 콘솔 출력
console.log(window.innerHeight) 
// html 콘텐츠 문서의 높이
doc_h = nav_h + con_h + footer_h
// 높이의 따른 fixed-bottom 처리
console.log(doc_h)
if (doc_h >= window.innerHeight){
  document.querySelector('footer').classList.remove('fixed-bottom')
}
// else if (800 <= window.innerHeight) {
//   document.querySelector('footer').classList.remove('fixed-bottom')
// }