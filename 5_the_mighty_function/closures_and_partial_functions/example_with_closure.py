from dataclasses import dataclass
from typing import Callable

@dataclass
class Applicant:
    num_siblings: int

def get_admission_probability(applicant: Applicant, priority: Callable[[Applicant], bool]) -> float:
    if priority(applicant=applicant):
        return 0.5
    else:
        return 1.0

def has_priority(sibling_cutoff: int) -> Callable[[Applicant], bool]:
    def has_few_sibling(applicant: Applicant) -> bool:
        return applicant.num_siblings < sibling_cutoff
    return has_few_sibling

def main() -> None:
    applicants = [
        Applicant(1), Applicant(3)
    ]
    print(get_admission_probability(applicant=applicants[0], priority=has_priority(2)))
    print(get_admission_probability(applicant=applicants[1], priority=has_priority(3)))

if __name__ == '__main__':
    main()