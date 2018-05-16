import * as m from 'mithril';
import { STEP_ENDPOINT, STEPS_ENDPOINT } from './constants';

type Step = string;

interface IStepManager {
    getSteps(): Promise<Step[]>;
    addStep(step: Step): Promise<Step[]>;
    deleteStep(step: Step): Promise<Step[]>;
}

const stepManager: IStepManager = {
    getSteps: (): Promise<Step[]> => {
        return m.request({
            method: 'GET',
            url: STEPS_ENDPOINT,
        });
    },
    addStep: (step: Step): Promise<Step[]> => {
        const formData: FormData = new FormData();
        formData.append('step_text', step);

        return m.request({
            method: 'POST',
            url: STEP_ENDPOINT,
            data: formData,
        });
    },
    deleteStep: (step: Step): Promise<Step[]> => {
        const formData: FormData = new FormData();
        formData.append('step_text', step);

        return m.request({
            method: 'DELETE',
            url: STEP_ENDPOINT,
            data: formData,
        });
    },
}


export { Step, stepManager };
