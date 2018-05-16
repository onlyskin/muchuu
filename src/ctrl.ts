import { stepManager, Step } from './steps'

interface ICtrl {
    steps: Step[];
    randomStep(): Step;
    addStep(step: Step): void;
    deleteStep(step: Step): void;
};

class Ctrl implements ICtrl {
    steps: Step[];

    constructor() {
        this.steps = [] as Step[];
        stepManager.getSteps()
            .then((steps) => this.steps = steps);
    }

    randomStep(): Step {
        const index = Math.floor(Math.random()*this.steps.length);
        return this.steps[index];
    }

    addStep(step: Step): void {
        stepManager.addStep(step)
        .then((steps) => this.steps = steps);
    }

    deleteStep(step: Step): void {
        stepManager.deleteStep(step)
        .then((steps) => this.steps = steps);
    }
}

export { ICtrl, Ctrl };
