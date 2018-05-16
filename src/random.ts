import * as m from 'mithril';
import { ICtrl } from './page';
import { Step } from './steps';
import { AddStep } from './add_step';

const Random: m.Component<{
    ctrl: ICtrl
    step: Step,
}, {
    difficult: boolean,
}> = {
    oninit: (vnode) => {
        vnode.state.difficult = false;
    },
    view: (vnode) => {
        return m('.horizontal-container', m(
            '.vertical-container',
            [
                m(
                    '.step.padded.paper.h1-box',
                    vnode.attrs.step,
                ),
                m(
                    '.padded.paper.h1-box.clickable',
                    {
                        onclick: () => {
                            vnode.attrs.ctrl.deleteStep(
                                vnode.attrs.step
                            );
                            m.route.set('/');
                        },
                    },
                    'I did it!',
                ),
                m(
                    '.padded.paper.h1-box.clickable',
                    {onclick: () => vnode.state.difficult = true},
                    'I didn\'t do it...',
                ),
                vnode.state.difficult ? m(AddStep, {
                    ctrl: vnode.attrs.ctrl,
                    caption: 'Add a simpler step:',
                    callback: (step: Step): void => {
                        vnode.attrs.ctrl.addStep(step);
                        vnode.attrs.ctrl.deleteStep(vnode.attrs.step);
                        m.route.set('/');
                    },
                }) : null,
            ],
        ));
    },
};

export { Random };
