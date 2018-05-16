import * as m from 'mithril';
import { Page } from './page';
import { Random } from './random';
import { Ctrl } from './ctrl';

const ctrl = new Ctrl();

m.route(document.body, '/', {
    '/': {view: () => m(Page, {ctrl})},
    '/random': {
        oninit: (vnode) => {
            vnode.state.step = ctrl.randomStep();
        },
        view: (vnode) => m(Random, {
            ctrl,
            step: vnode.state.step,
        }),
    },
});
