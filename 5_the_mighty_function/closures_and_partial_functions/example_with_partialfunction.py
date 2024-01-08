from dataclasses import dataclass
from typing import Callable
from functools import partial

@dataclass
class Applicant:
    num_siblings: int

def get_admission_probability(applicant: Applicant, priority: Callable[[Applicant], bool]) -> float:
    if priority(applicant=applicant):
        return 0.5
    else:
        return 1.0

def has_priority(applicant: Applicant, sibling_cutoff: int) -> bool:
    return applicant.num_siblings < sibling_cutoff
    
def main() -> None:
    applicants = [
        Applicant(1), Applicant(3)
    ]
    has_few_sibling = partial(has_priority, sibling_cutoff = 3)
    print(get_admission_probability(applicant=applicants[0], priority=has_few_sibling))
    print(get_admission_probability(applicant=applicants[1], priority=has_few_sibling))

if __name__ == '__main__':
    main()