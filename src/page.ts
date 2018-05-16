import * as m from 'mithril';
import { AddStep } from './add_step';
import { ICtrl } from './ctrl';
import { Step } from './steps';

const Page: m.Component<{ctrl: ICtrl}, {}> = {
    view: (vnode) => {
        return m('.horizontal-container', m(
            '.vertical-container', 
            [
                m('.get-step.padded.paper.clickable', {
                    onclick: () => m.route.set('/random'),
                }, 'Take a step!'),
                m(AddStep, {
                    ctrl: vnode.attrs.ctrl,
                    caption: 'Add a step...',
                    callback: (step: Step): void => vnode.attrs.ctrl.addStep(step),
                }),
            ],
        ));
    },
};

export { Page, ICtrl };
