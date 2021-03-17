#!/usr/bin/env python3
from scripts.all_refactorings import AllRefactorings
from scripts.refactoring import Refactoring
from scripts.refactoring_category import RefactoringCategory

Refactoring.templates = Refactoring.create_templates()

if __name__ == '__main__':
    all = AllRefactorings()
    all.add_category(RefactoringCategory('Encapsulate', [
        'Encapsulate Field', ]))
    all.add_category(RefactoringCategory('Extract', [
        'Extract Class',
        'Extract Interface',
        'Extract Superclass', ]))
    all.add_category(RefactoringCategory('If Statements', [
        'Remove Redundant Else', ]))
    all.add_category(RefactoringCategory('Introduce', [
        'Introduce Field', ]))

    all.create_files()
