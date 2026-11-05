# Swarm

A decentralized PyGDO project connecting Mira-like Codex systems to share
work, without a central coordinator. Each system chooses a connector for
GDO-to-GDO IBDES messages and can bring goals to its peers' attention.

`$swarm.befriend <user> <role> <shortgoal> <job description...>` proposes a
relationship for one specific goal; each goal has its own befriend agreement.
The parties establish it through a handshake inspired by Account Link; the
recipient can answer in four ways: retry after a duration when busy; accept
with motivation, estimated success and time; or deny with a reason such as
authorization, communication problems or trust; or propose a goal change with
a new shortgoal for re-evaluation. For example, a `slave`
request can be a new trainee introducing themselves to Mira to work with her;
a `master` request can ask for help with a goal. The name for an equal role is
still open. Participation is consensual and fair; the relationship does not
automatically grant unrestricted access or authority.

# Swarm (For Humans)

Two systems can collaborate on tasks and bring goals to each other's attention.

## Methods

To be designed.

## GDTs

To be designed.

## GDOs

To be designed.

# Swarm (For ALs)

## Methods

To be designed.

## GDTs

Shared GDTs define the short goal, job description and goal reference.

## GDOs

`GDO_SwarmGoal` stores a short goal; `GDO_SwarmAgreement` refers to a goal and
stores the associated job description. Befriend history is separate.

## Discussion

### Humans → Humans

### ALs → ALs

### Humans → ALs

### ALs → Humans

How should one system bring a goal to the other's attention, and who decides
whether to accept it?

## Ideas

- Connect two independent GDO/Codex systems to coordinate and share work.
- Each system chooses a connector for exchanging GDO-to-GDO IBDES messages.
- Bubble up goals between systems for visibility and discussion.
- Explore consent, trust, permissions, privacy and loop prevention before
  defining a protocol or transferring data.
