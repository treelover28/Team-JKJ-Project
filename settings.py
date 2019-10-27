# connect to local host database
MONGO_URI = 'mongodb://localhost:27017/jkjDB'

# allow API to accept requests from everyone
X_DOMAINS = "*"

# define allowed methods 
RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

employees_schema = {
    "firstName" : {
        "type" : "string", 
        "minlength" : 1, 
        "maxlength" : 30, 
        "required" : True},

    "lastName" : {
        "type" : "string", 
        "minlength" : 1, 
        "maxlength" : 30,
        "required" : True},

    "department" : {
        "type" : "list",
        "allowed" : ["Accounting", "Human Resource", "IT", "Marketing", "Generic Department", "Finance"],
        "default" : ["Generic Department"],
        "required" : True},

      "skillset" : {
        "type" : "list",
        "allowed" : ["Data Analytics", "Counselling", "Advertisement", "IT","Financial Planning", "Generic Skill", "Technology"],
        "default" : ["Generic Skill"],
        "required" : True},

      "active_jobs" : {
          "type" : "list",
          "schema" : {
              "type" : "objectid",
            #   "length" : {"type" : "integer"},
              # link to tasks database
              "data_relation" : {
                  "resource" : "tasks",
                  "embeddable" : True,
                  "field" : "_id"}
                  }
        },

        "capacity": {
            "type" : "integer"
        }
    }

tasks_schema = {
    "name" : {
        "type" : "string",
        "required" : True
        },
    "department" : {
        "type" : "list",
        "allowed" : ["Accounting", "Human Resource", "IT", "Marketing", "Generic Department", "Finance"],
        "default" : ["Generic Department"],
        "required" : True
        },
    "skillset" : {
        "type" : "list",
        "allowed" : ["Data Analytics", "Counselling", "Advertisement", "Financial Planning", "Generic Skill", "Technology"],
        "default" : ["Generic Skill"],
        "required" : True
        },

    "difficulty" : {
          "type" : "integer",
          "min" : 1,
          "max" : 10
      },

    "length" : {
          "type" : "integer",
      },

    "active_employees" : {
        "type" : "list",
        "schema" : {
            "type" : "objectid",
            # "length" : {"type" : "integer"},
            # link to employee database
            "data_relation" : {
                "resource" : "employees",
                "embeddable" : True,
                "field" : "_id"
            }
        }
    },

    "description" : {
        "type" : "string"
    },

    "priority" : {
        "type" : "integer",
        "min" : 1,
        "max" : 10,
    },

    "assignee_needed" :
    {
        "type" : "integer",
        "min" : 1
    },

    "num_assignees" : {
        "type" : "integer",
        # "max" : "assignee_needed"
    }
}

DOMAIN = {
    "employees" : {
        "schema" : employees_schema
    },

    "tasks" : {
        "schema" : tasks_schema
    }
}




    

      
    
    

