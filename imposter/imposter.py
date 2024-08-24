import random
from datetime import datetime, timedelta
from pathlib import Path
import git
import click

@click.command()
@click.option('--repo-path', type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path), required=True, help='Path to the git repository')
@click.option('--days', type=int, default=30, help='Number of days to generate history for')
@click.option('--max-daily-commits', type=int, default=5, help='Maximum number of commits per day')
def main(repo_path: Path, days: int, max_daily_commits: int):
    """Generate fake git commit history."""
    repo = git.Repo(repo_path)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    click.echo(f"Generating fake git history for {days} days")
    click.echo(f"Repository path: {repo_path}")

    current_date = start_date
    while current_date <= end_date:
        num_commits = random.randint(0, max_daily_commits)
        for _ in range(num_commits):
            commit_time = current_date.replace(
                hour=random.randint(9, 23),
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )
            
            dummy_file = repo_path / "dummy_file.txt"
            with dummy_file.open("a") as f:
                f.write(f"Commit at {commit_time}\n")

            repo.index.add([str(dummy_file)])
            repo.index.commit(
                f"Commit at {commit_time}",
                author_date=commit_time,
                commit_date=commit_time
            )

        current_date += timedelta(days=1)

    click.echo("Fake git history generated successfully!")

if __name__ == "__main__":
    main()
