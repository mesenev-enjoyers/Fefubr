import {createRouter, createWebHashHistory} from "vue-router";
import LogAndReg from "@/components/LogAndReg";
import mainFeed from "@/components/MainFeed";
import UserFeed from "@/components/UserFeed";
import UsersChat from "@/components/UsersChat";
import UserProfile from "@/components/UserProfile";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {path: '/', component: mainFeed},
        {path: '/userfeed', component: UserFeed}, //Добавить получать ссылку,зависящую от юзера
        {path: '/chats', component: UsersChat},
        {path: '/profile', component: UserProfile}, //Добавить получать ссылку,зависящую от юзера
        {path: '/authorization', component: LogAndReg},
    ]
})