import {createRouter, createWebHashHistory} from "vue-router";
import MainPage from "@/Pages/MainPage";
import UserNews from "@/Pages/UserNews";
import UserChats from "@/Pages/UserChats";
import CreateUserPost from "@/Pages/CreateUserPost";
import LoginPage from "@/Pages/LoginPage";
import PostPage from "@/Pages/PostPage";

const routes = [
    {path: '/', component: MainPage},
    {path: '/mynews', component: UserNews},
    {path: '/chats', component: UserChats},
    {path: '/createpost', component: CreateUserPost},
    {path: '/login', component: LoginPage},
    {path: '/post/:id', component: PostPage}
]
const router = createRouter({
    routes,
    history: createWebHashHistory(process.env.BASE_URL)
})

export default router;
