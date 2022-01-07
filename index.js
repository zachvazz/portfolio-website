class Sections {
    sectionNum = 1;

    printSection = () => {
        console.log(this.sectionNum);
    }
}

class Title extends Sections{
    fontFamily = 'Courier';
    printFontFamily = () => {
        console.log(this.fontFamily);
    }
}

const research = new Title();
research.printSection();
research.printFontFamily();