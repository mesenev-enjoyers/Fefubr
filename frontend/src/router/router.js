import {createRouter, createWebHashHistory} from "vue-router";
import MainPage from "@/Pages/MainPage";
import UserNews from "@/Pages/UserNews";
import UserChats from "@/Pages/UserChats";
import CreateUserPost from "@/Pages/CreateUserPost";
import LoginPage from "@/Pages/LoginPage";
import PostPage from "@/Pages/PostPage";
import RegPage from "@/Pages/RegPage";
import UserPage from "@/Pages/UserPage";
import TagPage from "@/Pages/TagPage";



const routes = [
    {path: '/', component: MainPage, name: 'MainPage'},
    {path: '/mynews', component: UserNews},
    {path: '/chats', component: UserChats},
    {path: '/createpost', component: CreateUserPost},
    {path: '/login', component: LoginPage, name: 'LoginPage'},
    {path: '/post/:id', component: PostPage},
    {path: '/register', component: RegPage},
    {path: '/user/:id', component: UserPage},
    {path: '/tag/:id', component: TagPage}
]
const router = createRouter({
    routes,
    history: createWebHashHistory(process.env.BASE_URL)
})

export default router;
