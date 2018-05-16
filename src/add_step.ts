import * as m from 'mithril';
import { ICtrl } from './page';
import { Step } from './steps';

const AddStep: m.Component<{
    ctrl: ICtrl,
    caption: string,
    callback: (step: Step) => void,
}, {step: Step}> = {
    view: (vnode) => {
        return m(
            '.add-step.padded.paper.h2-box',
            [
                m('.caption', vnode.attrs.caption),
                m(
                    'form',
                    {onsubmit: (e: Event) => {
                        e.preventDefault();
                        vnode.attrs.callback(vnode.state.step);
                        vnode.state.step = '';
                    }},
                    m('input[type=text]', {
                        oninput: m.withAttr(
                            'value',
                            (step) => vnode.state.step = step
                        ),
                        value: vnode.state.step,
                    }),
                ),
            ],
        );
    },
}

export { AddStep };
