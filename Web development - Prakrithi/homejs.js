
const showMenu = (toggleId, navId)=>{
  const toggle = document.getElementById(toggleId),
  nav= document.getElementById(navId)

  if(toggle && nav){
    toggle.addEventListener('click', ()=>{
      nav.classList.toggle('show')
    })
  }
}

showMenu('nav-toggle','nav-menu')


const navLink = document.querySelectorAll('.nav__link'),
  navMenu = document.getElementById('nav-menu')

function linkAction(){
  navMenu.classList.remove('show')
}

navLink.foreach(n => n.addEventListener('click',linkAction))


window.onscroll = ()=>{
  const nav = document.getElementById('header')
  if(this.scrollY>=200) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
