import './style';
import { h, render } from "preact";
import App from './components/app';

import ReviewinClient from "./api-dummy"
window.rvwnClient = new ReviewinClient();


render(<App />, document.body)