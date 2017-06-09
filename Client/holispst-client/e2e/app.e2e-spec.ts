import { HolispstClientPage } from './app.po';

describe('holispst-client App', function() {
  let page: HolispstClientPage;

  beforeEach(() => {
    page = new HolispstClientPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
