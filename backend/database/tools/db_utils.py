from psycopg2 import OperationalError
from core.logging import setup_logger
from database.services.setup import create_users_table, create_tokens_table

logger = setup_logger(__name__)


def test_db_connection(connection_manager):
    try:
        conn = connection_manager.request_conn()
        if conn:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1;")

                    logger.info("Connexion à la base de données réussie.")

                    cur.execute("""
                        SELECT table_name
                        FROM information_schema.tables
                        WHERE table_schema = 'public';
                    """)

                    tables = cur.fetchall()

                    if not tables:
                        logger.info("Création des tables dans la BDD")
                        create_users_table(connection_manager)
                        create_tokens_table(connection_manager)

            connection_manager.drop_conn(conn)

            return True
    except OperationalError as e:
        logger.error(f"Impossible de se connecter à la base de données: {e}")
        return False
    except Exception as e:
        logger.error(f"Erreur inattendue lors du test de la base de données: {e}")
        return False
