from frame.db import Db
from frame.sql import Sql
from frame.value import Res

class ResDb(Db):
    def insert(self,id,result):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.resultinsert % (id,result));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.resultlist);
        result = cursor.fetchall();
        for c in result:
            res = Res(c[0],c[1],c[2],c[3]);
            all.append(res);
        super().close(cursor,conn);
        return all;

if __name__ == '__main__':
    result=ResDb().select();
    for r in result:
        print(r);


