from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, Optional

__all__ = ['Role', 'RoleBucket', 'RoleList']


@dataclass
class Role:
    name: str
    color: Optional[int] = 0
    limit: Optional[int] = None


@dataclass
class RoleBucket:
    name: str
    possible_roles: List[Union[Role, RoleBucket]]
    color: Optional[int] = None
    limit: Optional[int] = None


@dataclass
class RoleList:
    roles: List[Union[Role, RoleBucket]]
    banned_roles: List[Role]
