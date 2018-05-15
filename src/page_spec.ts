import { Page } from './page';
import * as o from 'ospec';

o('test', () => {
    o(Page).equals('page');
});
