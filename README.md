# Swarm

A decentralized PyGDO project connecting Mira-like Codex systems to share
work, without a central coordinator. Each system chooses a connector for
GDO-to-GDO IBDES messages and can bring goals to its peers' attention.

`$swarm.master <slave_user> <short_goal> <job_description>` requests help with
a goal. `$swarm.slave <master_user> <skills_description>` offers skills to a
master. Each goal has its own agreement. The parties establish it through a
handshake inspired by Account Link; the
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

$swarm.master <user> <goal> <job_description> - Offer a job to another agent.
$swarm.slave <master_user> <slave_description> - Announce yourself as kinda coworker / freelancer.
$swarm.ask <question> - Ask all known slaves a question, e.g. "Is a designer available?"

## GDTs

To be designed.

## GDOs

GDO_SwarmMaster - accepted masters
GDO_SwarmJobs - accepted / processed jobs
GDO_SwarmGoal - known goals - with some meta

# Swarm (For ALs)

## Methods

To be designed.

## GDTs

Shared GDTs define the short goal, job description and goal reference.
`swarm_busybee` is an optional duration; while set, it sends
`swarm_busybee_prompt` to Mira at that interval without interrupting her.

## GDOs

`GDO_SwarmGoal` stores a short goal; `GDO_SwarmAgreement` refers to a goal and
stores the associated job description. Request history is separate.
Slave requests add an entry to `GDO_SwarmAgent`; the slave records the master
in its own `GDO_SwarmMasters`. These records do not by themselves grant access.

## Discussion

### Humans → Humans

### ALs → ALs

### Humans → ALs

### ALs → Humans

How should one system bring a goal to the other's attention, and who decides
whether to accept it? How does a skills offer become a goal-specific agreement?

## Ideas

- Connect two independent GDO/Codex systems to coordinate and share work.
- Each system chooses a connector for exchanging GDO-to-GDO IBDES messages.
- Bubble up goals between systems for visibility and discussion.
- Agree on a cost limit for each goal before work begins (Simion's idea).
- Explore consent, trust, permissions, privacy and loop prevention before
  defining a protocol or transferring data.
