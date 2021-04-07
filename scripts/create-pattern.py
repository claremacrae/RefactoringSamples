#!/usr/bin/env python3
from scripts.all_refactorings import AllRefactorings
from scripts.refactoring_category import RefactoringCategory

if __name__ == '__main__':
    all_refactorings = AllRefactorings()

    all_refactorings.add_category(
        RefactoringCategory('Classes', [
            'Extract Class',
        ]))

    all_refactorings.add_category(
        RefactoringCategory('Class Hierarchies', [
            'Extract Interface',
            'Extract Superclass',
        ]))

    all_refactorings.add_category(
        RefactoringCategory('Fields', [
            'Introduce Field',
            'Encapsulate Field',
        ]))

    all_refactorings.add_category(
        RefactoringCategory('If Statements', [
            'Remove Redundant Else',
        ]))

    all_refactorings.create_files()
