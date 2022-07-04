import {createRouter, createWebHashHistory} from "vue-router";
import MainPage from "@/Pages/MainPage";
import UserNews from "@/Pages/UserNews";
import UserChats from "@/Pages/UserChats";
import CreateUserPost from "@/Pages/CreateUserPost";
import LoginPage from "@/Pages/LoginPage";
import PostPage from "@/Pages/PostPage";
import RegPage from "@/Pages/RegPage";


const isAuthorized = localStorage.getItem('token') !== null;

const authGuard = function (to, from, next) {
    if (!isAuthorized) next({name: 'LoginPage'});
    else next()
}

const routes = [
    {path: '/', component: MainPage, name: 'MainPage'},
    {path: '/mynews', component: UserNews, beforeEnter: authGuard},
    {path: '/chats', component: UserChats, beforeEnter: authGuard},
    {path: '/createpost', component: CreateUserPost, beforeEnter: authGuard},
    {path: '/login', component: LoginPage, name: 'LoginPage'},
    {path: '/post/:id', component: PostPage},
    {path: '/register', component: RegPage}
]
const router = createRouter({
    routes,
    history: createWebHashHistory(process.env.BASE_URL)
})

export default router;
